package com.chapter.groups;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

@Test(groups = "student")
public class StudentTest {
    @BeforeMethod
    public void beforeMethodOnStudent() {
        System.out.println("准备学生分组测试数据---");
    }

    @AfterMethod
    public void afterMethodOnStudent() {
        System.out.println("清理学生分组测试数据---");
    }

    public void testCase1() {
        System.out.println("执行 student1 测试用例~~~");
    }

    public void testCase2() {
        System.out.println("执行 student2 测试用例~~~");
    }

    public void testCase3() {
        System.out.println("执行 student3 测试用例~~~");
    }
}
