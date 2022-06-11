use iced::{button, Alignment, Button, Column, Element, Sandbox, Settings, Text, Row, Length, Space, Size};

pub fn main() -> iced::Result {
    FrontendState::run(Settings::default())
}

#[derive(Default)]
struct FrontendState {
    value: i32,

    // Navigation buttons
    home_button: button::State,
    facebook_button: button::State,
    reddit_button: button::State,
    twitter_button: button::State,
}

#[derive(Debug, Clone, Copy)]
enum Message {
    HomePressed,
    FacebookPressed,
    RedditPressed,
    TwitterPressed,
}

impl Sandbox for FrontendState {
    type Message = Message;

    fn new() -> Self {
        Self::default()
    }

    fn title(&self) -> String {
        String::from("Severus Scrape")
    }

    fn update(&mut self, message: Message) {
        match message {
            Message::HomePressed => {

            }
            Message::FacebookPressed => {

            }
            _ => {}
        }
    }

    fn view(&mut self) -> Element<Message> {
        let spacing = 10;

        Column::new()
            .padding(spacing)
            .align_items(Alignment::Center)
            .push(Row::new()
                .height(Length::Fill)
            )
            .push(Row::new()
                .height(Length::Units(100))
                .align_items(Alignment::Center)
                .push(
                    // Bottom nav panel
                    Button::new(&mut self.home_button, Text::new("HOME"))
                        .on_press(Message::FacebookPressed)
                )
                .push(
                    // Bottom nav panel
                    Button::new(&mut self.facebook_button, Text::new("-"))
                        .on_press(Message::FacebookPressed)
                )
                .push(
                    // Bottom nav panel
                    Button::new(&mut self.reddit_button, Text::new("-"))
                        .on_press(Message::FacebookPressed)
                )
                .push(
                    // Bottom nav panel
                    Button::new(&mut self.twitter_button, Text::new("-"))
                        .on_press(Message::FacebookPressed)
                )
            ).into()
    }
}