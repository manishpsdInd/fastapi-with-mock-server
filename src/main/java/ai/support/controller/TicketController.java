package ai.support.controller;

import ai.support.model.TicketAnalysisResult;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.converter.BeanOutputConverter;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TicketController {

    private final ChatClient chatClient;

    public TicketController(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    @GetMapping("/api/tickets/analyze")
    public TicketAnalysisResult analyzeTicket(@RequestParam(value = "description") String description) {
        var converter = new BeanOutputConverter<>(TicketAnalysisResult.class);

        // Establishing a strict enterprise IT persona using the system directive
        String systemInstructions = """
            You are a tier-3 automated IT support ticket triage system.
            Analyze the incoming issue accurately.
            Categorize strictly according to technical impact.
            """;

        return this.chatClient.prompt()
                .system(systemInstructions) // Establishes the hidden AI background persona
                .user(description + "\n" + converter.getFormat())
                .call()
                .entity(converter);
    }

}
