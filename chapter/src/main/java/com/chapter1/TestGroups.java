package com.chapter1;

import org.testng.annotations.AfterGroups;
import org.testng.annotations.BeforeGroups;
import org.testng.annotations.Test;

public class TestGroups {
    // 测试用例分组需要添加参数制定分组名称

    @Test(groups = "server")
    public void testCase1() {
        System.out.println("服务端测试用例-1");
    }

    @Test(groups = "server")
    public void testCase2() {
        System.out.println("服务端测试用例-2");
    }

    @Test(groups = "server")
    public void testCase3() {
        System.out.println("服务端测试用例-3");
    }

    @Test(groups = "client")
    public void testCase4() {
        System.out.println("客户端测试用例-4");
    }

    @Test(groups = "client")
    public void testCase5() {
        System.out.println("客户端测试用例-5");
    }

    @Test(groups = "client")
    public void testCase6() {
        System.out.println("客户端测试用例-6");
    }

    // 分组运行需要添加注解参数执行用于指定测试用例组
    @BeforeGroups(groups = "server") // 该注解表示该组测试用例执行之前的方法
    public void beforeGroupsOnServer() {
        System.out.println("beforeGroupsOnServer: 服务端测试分组执行之前初始化测试环境~~~");
    }

    @AfterGroups(groups = "server") // 该注解表示该组测试用例执行之后的方法
    public void afterGroupsOnServer() {
        System.out.println("afterGroupsOnServer: 服务端测试分组执行之后清理测试环境~~~");
    }

    @BeforeGroups(groups = "client")
    public void beforeGroupsOnClient() {
        System.out.println("beforeGroupsOnClient: 客户端测试分组执行之前初始化测试环境~~~");
    }

    @AfterGroups(groups = "client")
    public void afterGroupsOnClient() {
        System.out.println("afterGroupsOnClient: 客户端测试分组执行之后清理测试环境~~~");
    }
}
