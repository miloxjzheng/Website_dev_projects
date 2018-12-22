package com.block72.common;

/**
 * Created by Jiateng on 5/28/18.
 */
public enum ErrorCode {

    SUCCESS(1, "success"),

    FAIL(-1, "fail"),

    PARAM_ERR(2, "parameter error"),

    TIME_OUT(3, "time out"),

    INTERNAL_ERR(4, "internal error");

    private int code;
    private String msg;

    ErrorCode(int code, String msg) {
        this.code = code;
        this.msg = msg;
    }

    public int getCode() {
        return code;
    }

    public String getMsg() {
        return msg;
    }
}
