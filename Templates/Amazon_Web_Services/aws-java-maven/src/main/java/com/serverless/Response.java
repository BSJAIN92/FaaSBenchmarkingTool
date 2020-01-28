package com.serverless;

import java.util.Map;
import java.time.LocalDateTime;

public class Response {

	private final String message;
	private final Map<String, Object> input;
	private long ExecutionStart;
	private long ExecutionEnd;

	public Response(String message, Map<String, Object> input, long ExecutionStart, long ExecutionEnd) {
		this.message = message;
		this.input = input;
		this.ExecutionStart = ExecutionStart;
		this.ExecutionEnd = ExecutionEnd;
	}

	public String getMessage() {
		return this.message;
	}

	public Map<String, Object> getInput() {
		return this.input;
	}

	public long getExecutionStart(){
		return this.ExecutionStart;
	}

	public long getExecutionEnd(){
		return this.ExecutionEnd;
	}
}
