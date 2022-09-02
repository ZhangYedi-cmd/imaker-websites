package com.zhang.model.request;

import com.zhang.base.request.PageRequest;
import lombok.Data;

@Data
public class SearchQuestionRequest extends PageRequest {
  private Integer questionId;
  private String title;
  private String detail;
  private String content;
}
