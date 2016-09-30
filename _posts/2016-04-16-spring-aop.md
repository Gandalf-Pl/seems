---
layout: post
title: 通过Spring的AOP实现权限和日志管理
---

### {{ page.title }}

最近使用spring+springMVC+mybatis开发一个RESTFUL的后台管理系统,需要在Controller层对
用户进行权限的判定,同时需要记录下对应的操作日志,查看一些文章发现可以通过spring的AOP和springM
VC的拦截器实现该功能.本篇讲述使用spring的AOP来实现.

#### 具体实现方式

+ **首先需要定义一个annotation用来拦截Controller**
    
    {% highlight java %}
    import java.lang.annotation.*;

    /**
     *
     * Created by panlei on 3/28/16.
     */
    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    @Documented
    public @interface SystemControllerLog {
        String description() default "";
    }
    {% endhighlight %}
    
+ **创建一个对应该拦截器的切点类**

    {% highlight java %}
    @Aspect
    @Component
    public class SystemLogAspect {
    
        private static final Logger logger = Logger.getLogger(SystemLogAspect.class);
    
        @Pointcut("@annotation(tech.seems.annotation.SystemControllerLog)")
        public void controllerAspect(){
        }
    
        @Before("controllerAspect()")
        public void doBefore(JoinPoint joinPoint) {
            HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
            String content = joinPoint.getTarget().getClass().getName();
            String description = "";
            try {
                description = getControllerMethodDescription(joinPoint);
            }catch (Exception e) {
                logger.error("error msg is " + e.getMessage());
            }
            /*
            此处可以写下你的需要记录的操作日志相关的东西,以及如果你需要权限验证,也可以在此处进行
            */
            logger.info(" operate " + content + " description" + description + " uri is " + uri);
        }
    
        /**
         * 获取注解中对方法的描述信息 用于Controller层注解
         *
         * @param joinPoint 切点
         * @return 方法描述
         * @throws Exception
         */
        public  static String getControllerMethodDescription(JoinPoint joinPoint)  throws Exception {
            String targetName = joinPoint.getTarget().getClass().getName();
            String methodName = joinPoint.getSignature().getName();
            Object[] arguments = joinPoint.getArgs();
            Class targetClass = Class.forName(targetName);
            Method[] methods = targetClass.getMethods();
            String description = "";
            for (Method method : methods) {
                if (method.getName().equals(methodName)) {
                    Class[] clazzs = method.getParameterTypes();
                    if (clazzs.length == arguments.length) {
                        description = method.getAnnotation(SystemControllerLog. class).description();
                        break;
                    }
                }
            }
            return description;
        }
    }
    {% endhighlight %}
    
+ **定义完该切入点之后,可以在RESTFUL Controller中使用上述定义的拦截器**

    {% highlight java %}
    @RestController
    @RequestMapping("/test")
    public class TestController {
    
        private Logger logger = Logger.getLogger(TestController.class);
    
        @RequestMapping(method = RequestMethod.GET)
        @SystemControllerLog(description = "测试日志切面")
        public void testMethod(HttpServletRequest request) {
           /*
           Controller层的相关业务逻辑
           */ 
        }
    {% endhighlight %}
    
+ **完成上述操作之后需要在对应的dispatcher-servlet中自动注册**

    此处使用aspectj-autoproxy是为了通知spring使用cglib而不是jdk来生成代理方法,
    这样AOP可以拦截到Controller.
    
    同时需要注意配置在dispatcher-servlet中,否则将无法拦截到,具体原因如下:
    
    将其配置在了spring-context.xml 核心配置文件中，该配置文件会被ContextLoaderListenerclass加在，
    Spring会创建一个WebApplicationContext上下文，称为父上下文（父容器） ，
    保存在 ServletContext中，keyWebApplicationContext.ROOT_WEB_APPLICATION_CONTEXT_ATTRIBUTE的值。
    
    而spring-mvc.xml是DispatcherServlet,可以同时配置多个，每个 DispatcherServlet有一个自己的上下文对象（WebApplicationContext），
    称为子上下文（子容器），子上下文可以访问父上下文中的内容，但父上下文不能访问子上下文中的内容。 它也保存在 ServletContext中，key是"org.springframework.web.servlet.FrameworkServlet.CONTEXT"+Servlet名称
    
    当spring加在父容器的时候就会去找切入点，但是这个时候切入的controller是在子容器中的，父容器是无法访问子容器，所以就拦截不到。
    如果将上述的配置文件放到dispatcher-servlet.xml中，那么问题就解决了.
    
    具体代码如下:
    
    {% highlight xml %}
    <context:component-scan base-package="**.**.aspect"/>
    <mvc:annotation-driven/>
    <aop:aspectj-autoproxy proxy-target-class="true" />
    {% endhighlight %}
