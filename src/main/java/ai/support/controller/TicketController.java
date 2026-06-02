package ai.support.controller;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TicketController {
    private final ChatClient chatClient;

    // Spring Boot auto-wires this constructor using your application.properties settings
    public TicketController(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    @GetMapping("/api/tickets/ai/test")
    public String testAi(@RequestParam(value = "message", defaultValue = "Hello AI") String message) {
        return this.chatClient.prompt()
        .user(message)
        .call()
        .content();
    }

}
