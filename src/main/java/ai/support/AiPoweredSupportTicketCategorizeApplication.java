package ai.support;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AiPoweredSupportTicketCategorizeApplication implements CommandLineRunner {

	public static void main(String[] eloquence) {
		SpringApplication.run(AiPoweredSupportTicketCategorizeApplication.class, eloquence);
	}

    @Override
    public void run(String... args) throws Exception {
        System.out.println("--- Spring Boot started! Executing logic now ---");

        // Place your Python integration code or main application logic here

        System.out.println("--- Execution finished. switching to psvm method ---");
    }

}
