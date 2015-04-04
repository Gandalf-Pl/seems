---
layout: post
title: AndroidStudio学习安卓开发
---

###{{ page.title }}


　　Android是使用Task来管理活动的，一个任务就是一组存放在栈里的活动的集
合，这个栈也被称作为返回栈（Back Stack）。栈式一种后进先出的数据结
构。

　　每一个活动在其生命周期中最多可能有四种状态

* 运行状态
    + 当一个活动位于返回栈的栈顶时，这时活动处于运行状态，系统最不愿
    回收的就是处于运行状态的活动。
* 暂停状态
    + 当一个活动不再处于栈顶位置，但仍然可见时，这时活动就进入暂停状
    态。处于暂停状态的活动仍然式完全存活着的，系统也不愿意去回收这种
    活动。
* 停止状态
    + 当一个活动不再处于栈顶位置，并且完全不可见的时候，就进入了停止
    状态。系统仍然会为这种活动保存相应的状态和成员变量，但是这并不是
    完全可靠的，当其他地方需要内存时，处于停止状态的活动有可能会被系
    统回收。
* 销毁状态
    + 当一个活动从返回栈中移出后就变成了销毁状态。系统会最倾向于回
    收这种状态的活动。

Activity的生存期

1. onCreate()

    这个方法在活动第一次被创建的时候调用。应该在这个方法中完成活动的
    初始化操作，比如加载布局，绑定事件等。

2. onStart

    这个方法在活动由不可见变成可见的时候调用。

3. onResume

    这个方法在活动准备好和用户进行交互的时候调用。此时的活动一定位于
    返回栈的栈顶，并且处于运行状态

4. onPause

    这个方法在系统准备去启动或者恢复另一个活动的时候调用。通常会在这个
    方法中将一些消耗CPU的资源释放掉，以及保存一些关键数据，但是这个
    方法的执行速度一定要快，不然会影响到栈顶活动的使用。

5. onStop

    这个方法在活动完全不可见的时候调用。它和onPause的主要区别在与，
    如果穷的能够的新活动式一个对话框式的活动，那么onPause会执行，
    而onStop方法并不会执行。

6. onDestroy

    这个方法在活动被销毁之前调用，滞后活动的状态就成为销毁状态。

7. onRestart

    这个方法在活动由停止状态变成运行状态之前调用，也就是活动被重新
    启动。

上面的七个方法中除了onRestart外其他都是两两对应的。因此有可以将活动
分成三种生存期。

1. 可见生存期

    活动在onStart和onStop方法之间所经历的，就是可见生存期。在可见生
    存期内，活动对于用户总是可见的，即便有可能无法和用户进行交互。

2. 前台生存期

    活动在onResume和onPause之间所经历的就是前台生存期。在前台生存期
    活动总是处于运行状态，此时的活动是可以和用户进行交互的。

3. 完整生存期

    活动在onCreate和onDestroy之间经历的，就是完整生存期。

**活动的启动模式**

#####活动的启动模式共有四种：

1. standard 
    standard是默认的启动模式

2. singleTop
    当活动的启动模式式singleTop，在启动该活动时如果发现返回的栈顶
    已经式该活动，则认为可以直接使用它而不再创建新的活动实例。

3. singleTask
    当活动的启动模式式singleTask时，每次启动该活动系统首先会在返回
    栈中检查是否存在该活动的实例，乳沟发现已经存在，则直接使用该实例
    ，并把在这个活动之上的活动统统出栈，如果么有发现就会创建一个新的
    活动实例。

4. singleInstance
    指定singleInstance模式的活动会启用一个新的返回栈来管理这个活动。
    采用这种模式可以解决共享活动实例的问题。

**Android中的四种最基本的布局**

1. LinearLayout

    线性布局，是一种非常常用的布局。这种布局会将它所包含的控件在线性
    方向上一次排列。
    
    通过android:orientation属性可以指定派来方向(vertical & horizontal)
    如果没有指定orientation属性的值，默认的排列方向就是horizontal。
    
    如果排列方向式horizontal，内部的控件就绝对不能将宽度指定为
    match_parent,因为这样的话单独一个控件就会将整个水平方向占满，
    其他的控件就没有位置可以放置了。同理，如果排列方向式vertical，内
    部的控件就不能将高度指定为match_parent。

    关键属性的用法：
    
    + android:layout_gravity
    
        用于指定控件在布局中的对齐方式。

    + android:gravity
    
        用于指定文字在控件中的对齐方式。

    + android:layout_weight
    
        这个属性允许我们使用比例的方式来指定控件的大小，它在手机屏幕的
        适配性方面可以起到非常重要的作用。
        使用layout_weigh属性之后，控件的宽度就不再受android:layout_width
        来决。此时layout_width指定为0是一种比较规范的写法。

2. RelativeLayout

    相对布局，也是一种非常常用的布局。相对布局可以通过相对定位的方式
    让控件出现在布局的任何位置。

    关键属性的用法：
    
    + android:layout_above 
    
        让一个控件在另一个控件的上方。需要为这个属性指定相对控件id
        的引用。

    + android:layout_below
    
        表示让控件位与另一个控件的下方。

    + android:layout_toLeftOf
    
        表示让一个控件位与另一个控件的左侧。

    + android:layout_toRightOf
    
        表示让一个控件位于另一个控件的右侧

    + android:layout_alignLeft
    
        表示控件让另一个控件的左边缘和另一个控件的左边缘对齐。

    + android:layout_alignRight

    + android:layout_alignTop

    + android:layout_alignBottom

3. FrameLayout

    这种布局没有任何的定位方式，所有的控件都会摆放在布局的左上角。

4. TableLayout

    这种布局允许我们使用表格的方式来排列控件，这种布局也不是很常用。

    android:stretchColumns=”1”
    
    表示如果表格不能完全占满屏幕宽度，就将第二行进行拉伸。这里指定成
    1就是拉伸第二列，0拉伸第一列，类推。

**控件和布局的继承结构**

一些其他的属性：

    + android:background 

        用于为布局或控件指定一个背景，可以使用颜色或图片来进行填充。

    + android:layout_margin
        
        这个属性，它可以指定控件在上下左右方向上偏移的距离.

    + android:layout_marginLeft
        
    + android:layout_marginTop

        这几个属性可以用来单独指定控件在某个方向上的偏移的距离。

通过include可以非常方便的引用一个布局，同时解决了重复编写布局代码的问
题，但是如果布局中有一些控件要求能够响应时间，我们还是需要在每个活动
中为这些控件单独编写一次时间注册的代码。

**最常用的控件ListView**

ListView允许用户通过手指上下华东的方式将屏幕外的数据滚动到屏幕内，
同时屏幕上原有的数据则会滚出屏幕.

数组的数据是无法直接出传递给ListView的，我们还需要借助适配器来完成。
android提供了很多适配器的实现类，ArrayAdapter可以通过泛型来指定要
适配的数据类型，然后在构造函数中把要适配的数据传入即可。

android.R.layout.simple_list_item_1是一个android的内置的布局文件，
里面只有一个TextView，可以用于显示一段文本。

Android中的单位和尺寸

+ px 

    pｘ是像素的意思，即屏幕中可以显示的最小元素单元。

+ pt
    
    pt是磅数的意思，１磅== 1/72英寸。

+ dp
    
    dp 也是dip，是密度无关像素的意思。它在不同密度的屏幕中的显示比例
    将保持一致。

+ sp

    sp是可伸缩像素的意思。

**碎片和活动之间进行通信**

为了方便碎片和活动之间进行通信，FragmentManager提供了一个类似于
findViewById()的方法专门用于从布局文件中获取碎片的实例。

*example code:*

    RightFragment RightFragment = (Rightfragment) getFragmentManger().findFragmentById(R.id.right_fragment);

通过调用FragmentManager的findFragmentById()方法，可以在活动中得到相应
碎片的实例，然后就能轻松的调用碎片李宓的方法。

碎片(Frag)中如何调用活动里的方法，在每个碎片中都可以通过调用
getActivity()方法来得到和当前碎片相关联的活动实例

*example code:*

    MainActivity activity = (MainActivity) getActivity();

有了活动实例之后，在碎片中调用活动里的方法就变得轻而易举。另外当碎片中
需要使用Context对象的时候，也可以使用getActivity()方法，因为获取到
的活动本身就是一个Context对象了。

**碎片的生命周期(Fragment)**

1. 运行状态
    
    当一个碎片是可见的，并且它所关联的活动正处于运行状态时，该碎片也
    处于运行状态。

2. 暂停状态

    当一个活动进入暂停状态，与它相关联的可见碎片就会进入到暂停状态

3. 停止状态

    当一个活动进入停止状态时，与它相关联的碎片就会进入到停止状态，
    或者通过调用FragmentTransaction的remove(), replace()方法将碎片从
    活动中移出，但有在事务提交前调用addToBackStack()方法，此时碎片也进入
    到暂停状态。

4. 销毁状态

    碎片总是依附于活动而存在的,因此当活动被销毁时,与它相关联的碎片就会进入
    到销毁状态。或者通过调用 FragmentTransaction 的 remove()、replace()方法将碎片从活
    动中移除,但在事务提交之前并没有调用 addToBackStack()方法,这时的碎片也会进入
    到销毁状态。

**活动中有的回调方法,碎片中几乎都有,不过碎片还提供了一些附加的回调方法**

1. onAttach()
    
    当碎片和活动建立关联的时候调用。

2. onCreateView()

    为碎片创建视图(加载布局)时调用。

3. onActivityCreated()

    确保与碎片相关联的活动一定已经创建完毕的时候调用。

4. onDestroyView()

    当与碎片关联的视图被移除的时候调用。

5. onDetach()

    当碎片和活动解除关联的时候调用.


![控件和布局的继承结构](../images/view&viewgroup.png)

