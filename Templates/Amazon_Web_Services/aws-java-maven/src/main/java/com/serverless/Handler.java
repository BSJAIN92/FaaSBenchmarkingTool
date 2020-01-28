package com.serverless;

import java.util.Collections;
import java.util.Map;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.LocalDate;
import java.time.ZonedDateTime;


import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import code_logic.code_logic;

public class Handler implements RequestHandler<Map<String, Object>, ApiGatewayResponse> {

	private static final Logger LOG = LogManager.getLogger(Handler.class);

	@Override
	public ApiGatewayResponse handleRequest(Map<String, Object> input, Context context) {
		LOG.info("received: {}", input);
		
		ZoneId zoneId = ZoneId.of("GMT");

		LocalDateTime ES = LocalDateTime.now();

		int i = code_logic.code();

		LocalDateTime EE = LocalDateTime.now();

		long ExecutionStart = ES.atZone(zoneId).toInstant().toEpochMilli();

		long ExecutionEnd = EE.atZone(zoneId).toInstant().toEpochMilli();

		Response responseBody = new Response("Go Serverless v1.x! Your function executed successfully! Your result is: " + i, input, ExecutionStart, ExecutionEnd);
		return ApiGatewayResponse.builder()
				.setStatusCode(200)
				.setObjectBody(responseBody)
				.setHeaders(Collections.singletonMap("X-Powered-By", "AWS Lambda & serverless"))
				.build();
	}
}
