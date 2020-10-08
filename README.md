## TestNG测试框架学习记录

## Maven项目引入TestNG包

1. 官方网站下载TestNG包: https://mvnrepository.com/artifact/org.testng/testng

2. IDEA引入TestNG包

3. pom.xml配置文件新增

   ```xml
   <dependencies>
       <!-- https://mvnrepository.com/artifact/org.testng/testng -->
       <dependency>
           <groupId>org.testng</groupId>
           <artifactId>testng</artifactId>
           <version>7.0.0</version>
           <scope>test</scope>
       </dependency>
   </dependencies>
   ```

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
18. **@Test(timeOut = 3000)**:  该注解表示超时测试用例, 时间单位毫秒. 超过超时时间, 测试用例判定失败

## TestNG集成'ExtentReport'生成测试报告

1. 

