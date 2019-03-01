---
layout: post
title: 使用PowerMock编写单元测试
---


### 单元测试的目的

    单元测试的目的，是为了提高代码质量，保证代码的可维护性。因此我们在编写单元测试的时候，更多的是对代码逻辑的验证，查看
    是否能够对一些边界条件，特殊的逻辑完整的覆盖到。

    但是很多时候，我们的业务代码会进行一些IO操作(DB,CACHE,REMOTE-RPC)，这样导致单元测试的成本比较高。面对这样的场景的时候，
    我们可以通过Mock来简化我们的单元测试。

    由于单元测试最主要的是要覆盖业务逻辑，所以我们可以通过mock我们想要的一些边界值，来覆盖代码的各个业务逻辑分支，查看代码
    的处理是否和我们的预期一致。


### 为什么通过PowerMock进行单元测试的编写

    PowerMock是在基于Mockito的基础上，对mock功能扩充对静态方法，私有方法的mock处理。这样在在书写单元测试的时候，大大的降低了编写的成本。

### 如何通过PowerMock进行单元测试的编写

+ 例如我们需要进行单元测试的类:

    ~~~ python
    print("hello")
    ~~~

    ``` java
    @Service
    public class A {

        @Autowired
        private B b;

        private String privateMethod(String test) {
            System.out.println("private method");
            return "ok"
        }

        public String pubMethod(String test) {
            String var = b.getVar(test);
            return this.privateMethod(var);
        }
    }
    ```

    编写单元测试的时候，我们需要对A类进行测试，执行其中的public方法,同时需要mock掉对应的私有方法。

    在编写单元测试之前，我们需要知道injectMocks和Mock的区别
    @InjectMocks 用来注解需要测试的类。
    @Mock 用来注解需要测试的类中依赖的其他类。


    ~~~ java
    @RunWith(PowerMockRunner.class)
    public class ATest{

        @InjectMocks
        private A a;

        @Mock
        private B b;

        @Before
        public void setup() {
            a = PowerMockito.spy(new A()));
            MockitoAnnotations.initMocks(this);
        }

        @Test
        public void pubMethodTest() {
            PowerMockito.doReturn("test").when(a, "privateMethod", "test");
            PowerMockito.when(b.getVar("test")).thenReturn("test");
            String res = a.pubMethod()
            assertEquals(res, "test")
            // check private method 调用的次数是否和预期一致
            PowerMockito.verifyPrivate(a, Mockito.times(1)).invoke("privateMethod", "test");
        }
    }
    ~~~

    在上面的单元测试中，我们使用spy来对要测试的数据进行Mock，表示的是找个测试类中，有些方法我们需要mock，有些我们需要测试。如果不在setup中对A进行spy，在测试中我们就无法进行对私有方法的mock。

    上述在setup进行的操作也可以通过注解进行，但是需要注意注解的顺序,这样mockito就会先进行mock，然后进行spy


    ~~~ java
    @RunWith(PowerMockRunner.class)
    public class ATest {

        @InjectMocks
        @spy
        private A a;

        @Mock
        private B b;

        ......
    }
    ~~~

   当我们遇到如下需要测试的场景的时候，需要在测试类上加PrepareForTest注解。

    1. 当需要mock final方法的时候，必须加注解@PrepareForTest。注解@PrepareForTest里写的类是final方法所在的类。
    2. 当需要mock静态方法的时候，必须加注解@PrepareForTest。注解@PrepareForTest里写的类是静态方法所在的类。
    3. 当需要mock私有方法的时候, 需要加注解@PrepareForTest，注解里写的类是私有方法所在的类。测试类自己的私有方法可以不需要在这个注解中加。
    4. 当需要mock系统类的静态方法的时候，必须加注解@PrepareForTest。注解里写的类是需要调用系统方法所在的类。

    具体的使用姿势如下:

    ~~~ java
    @RunWith(PowerMockRunner.class)
    @PrepareForTest({B.class, C.class})
    public class ATest {
    }
    ~~~

