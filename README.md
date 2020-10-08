## TestNG测试框架学习记录
### TestNG基础注解讲解

1. **@Test**: 该注解表示所修饰方法是: 最基础测试方法
2. **@Ignore**: 该注解表示: 所修饰的方法是一个不会被执行(忽略)的测试用例
3. **@Test(enabled = false)**: 该注解表示: 所修饰的方法是一个不会被执行(忽略)的测试用例
4. **@BeforeMethod**: 该注解表示所修饰的方法是: 每一个 **测试用例(测试方法)** 执行 **之前** 都会执行的方法
5. **@AfterMethod**: 该注解表示所修饰的方法是: 每一个 **测试用例(测试方法)** 执行 **之后** 都会执行的方法
6. **@BeforeClass**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之前** 都会执行的方法
7. **@AfterClass**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之后** 都会执行的方法
8. **@BeforeSuite**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之前** 都会执行的方法 注意: BeforeSuite的执行要**早于**BeforeClass
9. **@AfterSuite**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之后** 都会执行的方法 注意: AfterSuite的执行要**晚于**AfterClass
10. **@BeforeTest**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之前** 都会执行的方法 注意: BeforeTest的执行要**早于** BeforeClass, **晚于** BeforeSuite
11. **@AfterTest**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之后** 都会执行的方法 注意: AfterTest的执行要**晚于**AfterClass, **早于**AfterSuite
12. **@Test(groups = "server")**: 该注解表示对测试用例进行分组, 需要指定组名
13. **@BeforeGroups(groups = "server")**: 该注解表示该组测试用例执行**之前**的方法
14. **@AfterGroups(groups = "server")**: 该注解表示该组测试用例执行**之后**的方法
15. **@Test(expectedExceptions = NullPointerException.class)**: 该注解表示该测试用例执行**之后**存在**预期的异常**
16. **@Test(dependsOnMethods ={ "testCase1", "testCase3"})**: 该注解表示:运行修饰的测试用例时会先执行依赖的测试用例, 如果依赖的测试**都**执行成功, 则会执行修饰的测试用例. 否则忽略修饰的测试用例; 如果所依赖的多个测试用例,依赖的测试用例之间相互独立互不不影响
17. **@Test(invocationCount = 15, threadPoolSize = 5)**: 该注解表示使用多线程执行该测试用例. 注意: 需要指定线程数大小以及线程池大小

### TestNG注解执行顺序

```java
/**
 * TestNG测试注解执行顺序:
 * BeforeSuite
 * 	   ↓
 * BeforeTest
 *     ↓
 * BeforeClass
 *     ↓
 * BeforeMethod
 *     ↓
 *    Test
 *     ↓
 * AfterMethod
 *     ↓
 * AfterClass
 *     ↓
 * AfterTest
 *     ↓
 * AfterSuite
 */
```

### TestNG配置文件

1. TestSuite配置xml文件内容

   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
   <suite name="testSuite">
       <test name="testLogin"> 标签: <test></test> 固定标签名
           <classes>
               <class name="com.chapter1.suite.SuiteConfig"/>
               <class name="com.chapter1.suite.LoginTest"/>
           </classes>
       </test>
       <test name="testPay">
           <classes>
               <class name="com.chapter1.suite.SuiteConfig" />
               <class name="com.chapter1.suite.PayTest" />
           </classes>
       </test>
   </suite>
   ```

2. TestGroups配置xml文件内容

   ```xml
   <?xml version="1.0" encoding="UTF-8" ?>
   <!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
   
   <suite name="testGroups">
   
   <!--    <test name="runAll">-->
   <!--        <classes>-->
   <!--            <class name="com.groups.StudentTest"/>-->
   <!--            <class name="com.groups.TeacherTest"/>-->
   <!--        </classes>-->
   <!--    </test>-->
   
       <test name="runStudent">
   <!--    分组运行测试用例    -->
           <groups>
               <run>
   <!--             指定运行的分组   -->
                   <include name="student"/>
               </run>
           </groups>
           <classes>
               <class name="com.chapter1.groups.StudentTest"/>
               <class name="com.chapter1.groups.TeacherTest"/>
           </classes>
       </test>
   </suite>
   ```

   