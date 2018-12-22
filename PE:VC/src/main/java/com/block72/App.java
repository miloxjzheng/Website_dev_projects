package com.block72;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


/**
 * Created by Jiateng on 10/19/18.
 */
@tk.mybatis.spring.annotation.MapperScan(basePackages = "com.block72.mapper")
@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
