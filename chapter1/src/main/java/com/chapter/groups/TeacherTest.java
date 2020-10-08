package com.chapter.groups;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

@Test(groups = "teacher")
public class TeacherTest {

    @BeforeMethod
    public void beforeMethodOnTeacher() {
        System.out.println("准备老师分组测试数据---");
    }

    @AfterMethod
    public void afterMethodOnTeacher() {
        System.out.println("清理老师分组测试数据---");
    }

    public void testCase1() {
        System.out.println("执行 teacher1 测试用例~~~");
    }


    public void testCase2() {
        System.out.println("执行 teacher2 测试用例~~~");
    }

    public void testCase3() {
        System.out.println("执行 teacher3 测试用例~~~");
    }
}
