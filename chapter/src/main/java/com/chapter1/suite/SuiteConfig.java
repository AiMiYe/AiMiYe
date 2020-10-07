package com.chapter1.suite;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeSuite;

public class SuiteConfig {

    @BeforeSuite
    public void beforeSuite(){
        System.out.println("初始化测试环境!!!");
    }

    @AfterSuite
    public void afterSuite(){
        System.out.println("清理测试环境!!!");
    }

    @BeforeMethod
    public void beforeMethod(){
        System.out.println("准备测试数据---");
    }

    @AfterMethod
    public void afterMethod(){
        System.out.println("清理测试数据--");
    }
}
