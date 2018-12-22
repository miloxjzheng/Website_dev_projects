package com.block72.common;


import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;


/**
 * Created by Jiateng on 5/30/18.
 */
@RestControllerAdvice
public class GlobalExceptionHandler {


    @ExceptionHandler(value = Exception.class)
    @ResponseBody
    public JsonResponse handleException(Exception e) {
        JsonResponse resp = null;
        if (e instanceof ServiceException) {
            ServiceException se = (ServiceException) e;
            resp = new JsonResponse(se.getErrCode(), se.getMsg());
        } else if (e instanceof MissingServletRequestParameterException) {
            resp = new JsonResponse(ErrorCode.PARAM_ERR.getCode(), e.getMessage());
        } else if (e instanceof MethodArgumentTypeMismatchException) {
            resp = new JsonResponse(ErrorCode.PARAM_ERR.getCode(), e.getMessage());
        } else if (e instanceof HttpRequestMethodNotSupportedException) {
            resp = new JsonResponse(ErrorCode.PARAM_ERR.getCode(), e.getMessage());
        } else if (e instanceof HttpMessageNotReadableException) {
            resp = new JsonResponse(ErrorCode.PARAM_ERR.getCode(), e.getMessage());
        } else {
            resp = new JsonResponse(ErrorCode.INTERNAL_ERR.getCode(), ErrorCode.INTERNAL_ERR.getMsg());
        }
        doLog(e);
        return resp;
    }

    /**
     * log output
     *
     * @param ex
     */
    private void doLog(Throwable ex) {

    }

}