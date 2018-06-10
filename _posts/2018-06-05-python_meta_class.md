Python的元类
============

* 类也是对象

    在理解Python的元类之前，你需要掌握Python的类相关的知识。Python的类，有一个借鉴自Smalltalk语言的特殊的概念。
    
    在大多数编程语言中，类就是一组描述如何生成对象的一段代码块。在Python中这一点也是成立的。
    
    ```
    >>> class ObjectCreator(object):
    ...       pass
    ...
    >>> my_object = ObjectCreator()
    >>> print(my_object)
    <__main__.ObjectCreator object at 0x8974f2c>
    ```
    
    但是，在Python中类还远不止这些功能，类也是对象，没错，对象。
    
    只要你使用关键字class修改，Python解释器会执行这代码代码，并创建一个对象，如:
    ```
    >>> class ObjectCreator(object):
    ...       pass
    ...
    ```
    
    这代码代码在执行的时候，会在内存中创建一个名为ObjectCreator的对象，这个对象(类)自身有创建对象(实例)的能力，这也是为什么它称之为类。
    但是，同时，它是一个对象，因此，你可以对它做如下操作:
    1. 你可以把它赋值给一个变量
    2. 你可以拷贝它
    3. 你可以给它添加属性
    4. 你可以把它当成一个函数的入参
    
    如：
    ```
    >>> print(ObjectCreator) # you can print a class because it's an object
    <class '__main__.ObjectCreator'>
    >>> def echo(o):
    ...       print(o)
    ...
    >>> echo(ObjectCreator) # you can pass a class as a parameter
    <class '__main__.ObjectCreator'>
    >>> print(hasattr(ObjectCreator, 'new_attribute'))
    False
    >>> ObjectCreator.new_attribute = 'foo' # you can add attributes to a class
    >>> print(hasattr(ObjectCreator, 'new_attribute'))
    True
    >>> print(ObjectCreator.new_attribute)
    foo
    >>> ObjectCreatorMirror = ObjectCreator # you can assign a class to a variable
    >>> print(ObjectCreatorMirror.new_attribute)
    foo
    >>> print(ObjectCreatorMirror())
    <__main__.ObjectCreator object at 0x8997b4c>
    ```
    
* 动态创建类

    既然类也是对象，那么你可以在运行时创建它们，就像你创建其他对象一样。
    首先，你可以创建在一个函数中使用class关键字创建一个类：
    ```
    >>> def choose_class(name):
    ...     if name == 'foo':
    ...         class Foo(object):
    ...             pass
    ...         return Foo # return the class, not an instance
    ...     else:
    ...         class Bar(object):
    ...             pass
    ...         return Bar
    ...
    >>> MyClass = choose_class('foo')
    >>> print(MyClass) # the function returns a class, not an instance
    <class '__main__.Foo'>
    >>> print(MyClass()) # you can create an object from this class
    <__main__.Foo object at 0x89c6d4c>
    ```
    但是这并不够动态，以为你仍然需要你自己写下完整的类。
    既然类是对象，那么它们肯定可以通过某种东西来生成。当你使用class关键字的时候，Python自动的创建这个类对象，但是和Python的大多数事情一样，它给了你手动创建的方法。
    还记的type函数么？这个古老但强大的函数能够让你知道一个对象的类型是什么，就像这样：
    ```
    >>> print(type(1))
    <type 'int'>
    >>> print(type("1"))
    <type 'str'>
    >>> print(type(ObjectCreator))
    <type 'type'>
    >>> print(type(ObjectCreator()))
    <class '__main__.ObjectCreator'>
    ```
    
    同时，type有一个完全不一样的功能，它可以在运行时创建类对象，type可以接收类的参数的描述信息，然后返回一个类。（我知道，根据传入参数的不同，同一个函数拥有两种完全不同的用法是一件很傻的事情，但这在Python中是为了保持向后兼容性）
    
    type这样工作：
    ```
    type(name of the class,
         tuple of the parent class (for inheritance, can be empty),
         dictionary containing attributes names and values)
    ```
    例如：
    ```
    >>> class MyShinyClass(object):
    ...       pass
    ```
    
    可以手动的这样创建:
    ```
    >>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
    >>> print(MyShinyClass)
    <class '__main__.MyShinyClass'>
    >>> print(MyShinyClass()) # create an instance with the class
    <__main__.MyShinyClass object at 0x8997cec>
    ```
    
    你注意到我们使用'MyShinyClass'作为类的名称，同时作为变量保存这个类的引用。它们可以不一样，但是我们没有理由来将问题复杂化。
    
    type接收一个字典来定义这个类的属性，所以：
    ```
    >>> class Foo(object):
    ...       bar = True
    ```
    也可以写成:
    ```
    >>> Foo = type('Foo', (), {'bar':True})
    ```
    然后可以当成正常的类来使用:
    ```
    >>> print(Foo)
    <class '__main__.Foo'>
    >>> print(Foo.bar)
    True
    >>> f = Foo()
    >>> print(f)
    <__main__.Foo object at 0x8a9b84c>
    >>> print(f.bar)
    True
    ```
    当然，你也可以继承它，如：
    ```
    >>>   class FooChild(Foo):
    ...         pass

    ```
    可以写成：
    ```
    >>> FooChild = type('FooChild', (Foo,), {})
    >>> print(FooChild)
    <class '__main__.FooChild'>
    >>> print(FooChild.bar) # bar is inherited from Foo
    True
    ```
    
    最后，如果你想为你的类添加方法，只需要定义一个有适当签名的函数，然后把它当成一个属性分配给它。
    ```
    >>> def echo_bar(self):
    ...       print(self.bar)
    ...
    >>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
    >>> hasattr(Foo, 'echo_bar')
    False
    >>> hasattr(FooChild, 'echo_bar')
    True
    >>> my_foo = FooChild()
    >>> my_foo.echo_bar()
    True
    ```
    你甚至可以在你动态创建完类之后给它添加更多的方法，就像一个正常创建的类添加方法一样：
    ```
    >>> def echo_bar_more(self):
    ...       print('yet another method')
    ...
    >>> FooChild.echo_bar_more = echo_bar_more
    >>> hasattr(FooChild, 'echo_bar_more')
    True
    ```
    现在你应该明白：在Python中，类都是对象，你可以在运行时动态的创建一个类。
    这就是当你使用关键字class的时候，Python所做的，而且是通过元类来做的。
    
* 什么是元类(metaclass)

    元类就是创建类的'职工'。你定义类来达到创建对象的目的，对么？但是我们已经知道Python类都是对象。
    
    好吧，元类就是用来创建这些类（对象）的，元类就是类的类，你可以这样想象它们：
    ```
    MyClass = MetaClass()
    my_object = MyClass()
    ```
    你已经知道type可以帮你做这样的事情:
    ```
    MyClass = type('MyClass', (), {})
    ```
    那是因为，事实上type函数就是一个元类，type就是Python用来在幕后创建所有类的元类。
    
    现在，你可能会好奇，为什么type是小写的，而不是**Type**?
    
    我猜测是因为为了保持一致性，就像str这个类用来创建所有的字符串对象，int用来创建所有的整数对象，type仅仅是用来创建类对象的类。
    
    你可以通过查看__class__属性来看看。
    
    所有的事情，在python中都是对象，包括ints, strings, functions和classes.所有的它们都是对象，所有的它们都是通过一个类创建的。
    ```
    >>> age = 35
    >>> age.__class__
    <type 'int'>
    >>> name = 'bob'
    >>> name.__class__
    <type 'str'>
    >>> def foo(): pass
    >>> foo.__class__
    <type 'function'>
    >>> class Bar(object): pass
    >>> b = Bar()
    >>> b.__class__
    <class '__main__.Bar'>
    ```
    
    那，__class__的__class__是什么呢？
    ```
    >>> age.__class__.__class__
    <type 'type'>
    >>> name.__class__.__class__
    <type 'type'>
    >>> foo.__class__.__class__
    <type 'type'>
    >>> b.__class__.__class__
    <type 'type'>
    ```
    所以，元类仅仅是用来创建类的东西，你可以把它称之为'class factory'。
    type是Python使用的内置的metaclass, 但是很正常，你可以创建你自己的元类。
    
* __metaclass__ 属性

    当你定义个类的时候，可以添加一个__metaclass__属性。
    ```
    class Foo(object):
    __metaclass__ = something...
    [...]
    ```
    
    如果你这么做，Python会使用这个metaclass来创建类Foo。小心，这个地方非常tricky。
    你首先定义了==class Foo(object)==,但是类对象Foo还没有在内存中创建。
    
    Python会去查找类定义中的__metaclass__,如果它找到了，它就会创建这个对象类Foo。如果没有，它就会使用type来创建这个类。
    
    多理解几遍.
    
    当你创建一个类：
    ```
    class Foo(Bar):
        pass
    ```
    Python会做如下这些操作：
    首先判定，在Foo中是否存在__metaclass__属性？
    如果存在，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象。如果Foo中找不到__metaclass__，它会在MODULE级别查找__metaclass__,然后阐释做同样的事情。
    如果它最终都没有找到任何的__metaclass__，它会使用它父类的metaclass来创建类对象。
    需要注意的是，__metaclass__属性是不能够被继承的，父类的元类是可以被继承的。如果Bar使用一个__metaclass__属性通过type()来创建(不是通过type.__new__())，子类不会继承这个行为。
    
    现在问题是，你可以放什么东西在__metaclass__中呢？
    答案是:能够创建一个类的东西。
    然而什么可以创建一个类呢？type，或者是其他子类，或者使用type。
    
* 自定义元类

    元类的主要目的是当一个类创建的时候，能够自动的修改这个类。
    
    当我们想创建一个匹配上线文信息的类的时候，我们平常都是通过API来处理。想想一个很傻的例子，当你决定你的模块中的所有的类的属性都应该是大写，有几种做法可以处理这样的事情，其中通过在模块级别设置__metaclass__可以达到目的。
    
    这种方式，模块中所有的类会使用元类来创建，我们仅仅需要告诉元类把所有的属性修改成大写即可。
    
    幸运的是，__metaclass__只要实际的能够调用就行，它不需要是一个正式的类，所以我们，通过使用function开始一个简单的例子。
    ```
    # the metaclass will automatically get passed the same argument
    # that you usually pass to `type`
    def upper_attr(future_class_name, future_class_parents, future_class_attr):
        """
          Return a class object, with the list of its attribute turned
          into uppercase.
        """
    
        # pick up any attribute that doesn't start with '__' and uppercase it
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
    
        # let `type` do the class creation
        return type(future_class_name, future_class_parents, uppercase_attr)
    
    __metaclass__ = upper_attr # this will affect all classes in the module
    
    class Foo(): # global __metaclass__ won't work with "object" though
        # but we can define __metaclass__ here instead to affect only this class
        # and this will work with "object" children
        bar = 'bip'
    
    print(hasattr(Foo, 'bar'))
    # Out: False
    print(hasattr(Foo, 'BAR'))
    # Out: True
    
    f = Foo()
    print(f.BAR)
    # Out: 'bip'
    ```
    现在，我们使用一个真实的类来实现元类，但是做的是同样的事情。
    ```
    # remember that `type` is actually a class like `str` and `int`
    # so you can inherit from it
    class UpperAttrMetaclass(type):
        # __new__ is the method called before __init__
        # it's the method that creates the object and returns it
        # while __init__ just initializes the object passed as parameter
        # you rarely use __new__, except when you want to control how the object
        # is created.
        # here the created object is the class, and we want to customize it
        # so we override __new__
        # you can do some stuff in __init__ too if you wish
        # some advanced use involves overriding __call__ as well, but we won't
        # see this
        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents, future_class_attr):
    
            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
    
            return type(future_class_name, future_class_parents, uppercase_attr)
    ```
    
    但是这不是真正的OOP。我们直接调用type，我们不去覆盖或者调用父类的__new__方法。
    ```
    class UpperAttrMetaclass(type):
    
        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents, future_class_attr):
    
            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
    
            # reuse the type.__new__ method
            # this is basic OOP, nothing magic in there
            return type.__new__(upperattr_metaclass, future_class_name,
                                future_class_parents, uppercase_attr)
    ```
    
    你可能已经注意到了有个额外的参数upperattr_metaclass，这并没有什么特别的。类方法的第一个参数总是表示当前的实例，就像在普通的类方法中的self参数一样。当然了，为了清晰起见，这里的名字我起的比较长。但是就像self一样，所有的参数都有它们的传统名称。因此，在真实的产品代码中一个元类应该是像这样的：
    
    ```
    class UpperAttrMetaclass(type):

        def __new__(cls, clsname, bases, dct):
    
            uppercase_attr = {}
            for name, val in dct.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
    
            return type.__new__(cls, clsname, bases, uppercase_attr)
    ```
    
    如果使用super方法的话，我们还可以使它变得更清晰一些，这会容易继承（是的，你可以拥有元类，从元类继承，从type继承）
    
    ```
    class UpperAttrMetaclass(type):

        def __new__(cls, clsname, bases, dct):
    
            uppercase_attr = {}
            for name, val in dct.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
    
            return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
    ```
    就是这样，除此之外，关于元类真的没有别的可说的了。使用到元类的代码比较复杂，这背后的原因倒并不是因为元类本身，而是因为你通常会使用元类去做一些晦涩的事情，依赖于自省，控制继承等等。确实，用元类来搞些“黑暗魔法”是特别有用的，因而会搞出些复杂的东西来。但就元类本身而言，它们其实是很简单的：
    1. 拦截一个类的创建
    2. 修改类
    3. 返回被修改之后的类
    
* 为什么使用元类而不是使用函数来代替？

    既然__metaclass__可以接受任何可以调用的对象，那为什么还要使用很明显更加复杂的类呢？
    这么做有几个原因：
    1. 意图会更加明显。当你看到UpperAttrMetaclass(type)的时候，你知道接下来将会怎么样。
    2. 你可以使用OOP。元类可以继承自元类，覆盖父类的方法，元类甚至可以使用元类。
    3. 如果你设置了一个元类的类，类的子类将会是它元类的实例。
    4. 你能够更好的组织你的代码。当你使用元类的时候肯定不会是像我上面举的这种简单场景，通常都是针对比较复杂的问题。将多个方法归总到一个类中会很有帮助，也会使得代码更容易阅读。
    5. 你可以使用__new__, __init__以及__call__这样的特殊方法。它们能帮你处理不同的任务。就算通常你可以把所有的东西都在__new__里处理掉，有些人还是觉得用__init__更舒服些。
    6. 该死，这东西的名字是metaclass，肯定非善类，我要小心！
    
* 为什么你要使用元类？

    那现在会我们的问题，为什么你会去使用这样一种容易出错且晦涩的特性？好吧，一般来说，你根本就用不上它：
    
    *“元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”*   —— Python界的领袖 Tim Peters
    
    元类的主要用途是创建API。一个典型的例子是Django ORM。它允许你像这样定义：
    ```
    class Person(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField()
    ```
    
    但是，如果你这样做：
    ```
    guy = Person(name='bob', age='35')
    print(guy.age)
    ```
    
    它不会返回一个IntegerField对象，他会返回一个int，甚至可以直接从数据库中取出数据。这大概是因为model.Model定义了__metaclass__，同时使用了一些魔法能够将你刚刚定义的简单的Person类转变成对数据库的一个复杂hook。Django框架将这些看起来很复杂的东西通过暴露出一个简单的使用元类的API将其化简，通过这个API重新创建代码，在背后完成真正的工作。
    
* 结束语

    首先，你知道了类其实是能够创建出类实例的对象。好吧，事实上，类本身也是实例，它们是元类的实例。
    ```
    >>> class Foo(object): pass
    >>> id(Foo)
    142630324
    ```
    在Python中，一切皆对象，他们要么是类的是实例，要么是元类的实例。
    除了type。
    type实际上是它自己的实例，在纯Python环境中这可不是你能够做到的，这是通过在实现层面耍一些小手段做到的。其次，元类是很复杂的。对于非常简单的类，你可能不希望通过使用元类来对类做修改。你可以通过其他两种技术来修改类：
    1. Monkey patching
    2. class decorators
    
    当你需要动态修改类时，99%的时间里你最好使用上面这两种技术。当然了，其实在99%的时间里你根本就不需要动态修改类。
    
翻译自StackOverflow上面一个同学的关于元类的回答。[英文原版](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
