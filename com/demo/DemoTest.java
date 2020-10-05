package com.demo;

import com.demo.Demo;
import com.demo.Options;
import org.junit.Test;

import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;


public class DemoTest {
    @Test
    public void testReflection() {
        Demo demo = new Demo(1,"6");
        System.out.println(demo);

        // 方式一
        Class<Demo> demoClass = Demo.class;

        // 获取类注解
        Options annotation = demoClass.getAnnotation(Options.class);
        System.out.println("类注解: " + annotation.value());
        // 获取类字段与注解
        try {
            Field field = demoClass.getField("x");
            Options fieldAnnotation = field.getAnnotation(Options.class);
            System.out.println("字段注解: "+ fieldAnnotation.value());
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        }

        // 获取类所有方法
        Method[] methods = demoClass.getMethods();
        ArrayList<String> strings = new ArrayList<>();
        for (Method method: methods){
            strings.add(method.getName());
        }
        System.out.println(strings);

        // 获取方法注解
        try {
            Method add = demoClass.getMethod("add", int.class, String.class);
            Options addAnnotation = add.getAnnotation(Options.class);
            System.out.println("方法注解: " + addAnnotation.value());
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        }

        // 调用方法
        try {
            Method method = demoClass.getMethod("setX", int.class);
            method.invoke(demo, 20);
            System.out.println(demo);
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
        // 方式二
        /*
        Class<? extends Demo> demoClass = demo.getClass();
        Options classAnnotation = demoClass.getAnnotation(Options.class);
        System.out.println("类注解: " + classAnnotation.value());

        // 获取字段
        try {
            Method method = demoClass.getMethod("add", int.class, String.class);
            int rlt = (int) method.invoke(demo, 5, "5");
            System.out.println(rlt);
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }

         */
    }
}
