package com.block72.common;



import com.block72.util.DateUtil;

import java.io.PrintWriter;
import java.io.StringWriter;

/**
 * Created by Jiateng on 5/29/18.
 */
public class ServiceException extends Exception {

    private int code;

    private String date = DateUtil.getCurrentTime(DateUtil.DateFormat.INTACT);

    private String message;

    public ServiceException(int errCode, String message) {
        super(message);
        this.code = errCode;
        this.message = message;
    }

    public int getErrCode() {
        return code;
    }

    public String getMsg() {
        return this.message;
    }

    public String getLogMessage() {
        return "[Error code]: " + code + "\n[Message]: " + super.getMessage() +
                "\n[Time]: " + date + "\n[Detail]: " + getCallStack();
    }

    private String getCallStack() {
        StringWriter sw = new StringWriter();
        this.printStackTrace(new PrintWriter(sw));
        return sw.toString();
    }
}
