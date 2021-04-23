package com.datasource;


import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;

import java.util.List;

public class JSONParse {
    private DocumentContext context = null;

    /**
     * @param jsonString JSON 字符串
     */
    public JSONParse(String jsonString) {
        if (jsonString != null || jsonString.equals("")) {
            this.context = JsonPath.parse(jsonString);
        }
    }

    /**
     * @param jsonPath jsonPath 表达式
     * @return 字符串 程序异常值返回 -1
     */
    public String getValue(String jsonPath) {
        if (jsonPath.startsWith("$.")) {
            String substring = jsonPath.substring(2).toUpperCase();
            char oneChar = substring.charAt(0);
            if (oneChar == 46) {
                char twoChar = substring.charAt(1);
                if (twoChar >= 65 && twoChar <= 90) {
                    try {
                        List<String> rlt = this.context.read(jsonPath);
                        if (rlt.size() > 0) {
                            return rlt.get(0);
                        }
                    } catch (ClassCastException e) {
                        e.printStackTrace();
                    }
                }
            }
            if (oneChar >= 65 && oneChar <= 90) {
                return this.context.read(jsonPath) + "";
            }
        }
        return "-1";
    }

    /**
     *
     * @param jsonPath jsonPath 表达式
     * @return 返回所有匹配到的值 程序异常值返回 null
     */
    public List<String> getValues(String jsonPath) {
        List<String> values = null;
        if (jsonPath.startsWith("$.")) {
            String substring = jsonPath.substring(2).toUpperCase();
            char oneChar = substring.charAt(0);
            if (oneChar == 46) {
                char twoChar = substring.charAt(1);
                if (twoChar >= 65 && twoChar <= 90) {
                    try {
                        values = this.context.read(jsonPath);
                    } catch (ClassCastException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
        return values;
    }

    public static void main(String[] args) {
        String string = "{\"code\":200,\"employees\": [{\"firstName\": \"George\",\"lastName\": \"Bush\"}," +
                "{\"firstName\": \"Thomas\",\"lastName\": \"Carter\"}],\"parse\":\"40.5\"}";

        JSONParse jsonParse = new JSONParse(string);
        List<String> values = jsonParse.getValues("$.code");
        System.out.println(values);
    }
}
