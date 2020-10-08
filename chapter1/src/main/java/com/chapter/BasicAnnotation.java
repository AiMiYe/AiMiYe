package com.chapter;

import org.testng.annotations.*;

/**
 * TestNG测试注解执行顺序:
 * BeforeSuite
 * ↓
 * BeforeTest
 * ↓
 * BeforeClass
 * ↓
 * BeforeMethod
 * ↓
 * Test
 * ↓
 * AfterMethod
 * ↓
 * AfterClass
 * ↓
 * AfterTest
 * ↓
 * AfterSuite
 */
public class BasicAnnotation {
    @Test // 该注解表示所修饰方法是: 最基础测试方法
    public void testCase2() {
        System.out.println("测试用例: " + (1 + 1));
    }

    @Test
    public void testCase3() {
        System.out.println("测试用例: " + (1 + 2));
    }

    // 方法一
    // @Ignore // 该注解表示: 所修饰的方法是一个不会被执行(忽略)的测试用例
    // 方法二
    @Test(enabled = false)
    public void testCase1() {
        System.out.println("测试用例: " + 1);
    }

    @BeforeMethod // 该注解表示所修饰的方法是: 每一个 *测试用例(测试方法)* 执行 *之前* 都会执行的方法
    public void beforeMethod() {
        System.out.println("**测试用例**执行之前需要执行的方法: beforeMethod");
    }

    @AfterMethod // 该注解表示所修饰的方法是: 每一个 *测试用例(测试方法)* 执行 *之后* 都会执行的方法
    public void afterMethod() {
        System.out.println("**测试用例**执行之后需要执行的方法: afterMethod");
    }

    @BeforeClass // 该注解表示所修饰的方法是: 每一个 *测试类* 执行 *之前* 都会执行的方法
    public void beforeClass() {
        System.out.println("**测试类**执行之前需要执行的方法: beforeClass");
    }

    @AfterClass // 该注解表示所修饰的方法是: 每一个 *测试类* 执行 *之后* 都会执行的方法
    public void afterClass() {
        System.out.println("**测试类**执行之后需要执行的方法: afterClass");
    }

    @BeforeSuite // 该注解表示所修饰的方法是: 每一个 *测试类* 执行 *之前* 都会执行的方法 注意: BeforeSuite的执行要早于BeforeClass
    public void beforeSuite() {
        System.out.println("**测试类**执行之前需要执行的方法: beforeSuite. 注意: BeforeSuite的执行要早于BeforeClass");
    }

    @AfterSuite // 该注解表示所修饰的方法是: 每一个 *测试类* 执行 *之后* 都会执行的方法 注意: AfterSuite的执行要晚于AfterClass
    public void afterSuite() {
        System.out.println("**测试类**执行之前需要执行的方法: afterSuite. 注意: AfterSuite的执行要晚于AfterClass");
    }

    @BeforeTest // 该注解表示所修饰的方法是: 每一个 *测试类* 执行 *之前* 都会执行的方法 注意: BeforeTest的执行要早于BeforeClass, 晚于BeforeSuite
    public void beforeTest() {
        System.out.println("beforeTest");
    }

    @AfterTest // 该注解表示所修饰的方法是: 每一个 *测试类* 执行 *之后* 都会执行的方法 注意: AfterTest的执行要晚于AfterClass, 早于AfterSuite
    public void afterTest() {
        System.out.println("afterTest");
    }
}
