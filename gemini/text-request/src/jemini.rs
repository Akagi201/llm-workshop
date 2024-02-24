use jemini::{JeminiClient, GeminiError, GeminiResponse};

#[tokio::main]
async fn main() -> Result<(), GeminiError> {
    let client = JeminiClient::new()?;
    let response: GeminiResponse = client.text_only("What is the meaning of life?").await?;

    dbg!(&response);
    println!("{}", response.most_recent().unwrap());

    Ok(())
}