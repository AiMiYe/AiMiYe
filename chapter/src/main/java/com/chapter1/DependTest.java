package com.chapter1;

import org.testng.annotations.Test;

public class DependTest {
    @Test
    public void testCase1(){
        System.out.println("运行 testCase1 测试用例---");
    }

    @Test(dependsOnMethods ={ "testCase1", "testCase3",  "testCase4"}) // 该注解表示:执行
    public void testCase2(){
        System.out.println("运行 testCase2 测试用例---");
    }

    @Test(expectedExceptions = NullPointerException.class)
    public void testCase3(){
        System.out.println("运行 testCase3 测试用例---");
        throw new NullPointerException();
    }
    @Test
    public void testCase4(){
        System.out.println("运行 testCase4 测试用例---");

    }
}
