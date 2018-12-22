package com.block72.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


/**
 * Views
 * Created by Jiateng on 10/19/18.
 */
@Controller
public class MainController {

    @GetMapping("/")
    public String index() {
        return "homepage";
    }

    @GetMapping("/contact")
    public String contact() {
        return "gbic-contact";
    }

    @GetMapping("/portfolio")
    public String subscribe() {
        return "gbic-portfolio";
    }

    @GetMapping("/career")
    public String policy() {
        return "gbic-career";
    }

    @GetMapping("/team")
    public String team() {
        return "gbic-team";
    }


}
