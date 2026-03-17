    #[test]
    fn test_color_red() {
        assert_eq!(Color::Red.to_string(), "#FF0000");
    }

    #[test]
    fn test_color_green() {
        assert_eq!(Color::Green.to_string(), "#00FF00");
    }

    #[test]
    fn test_color_blue() {
        assert_eq!(Color::Blue.to_string(), "#0000FF");
    }

    #[test]
    fn test_color_custom() {
        assert_eq!(Color::Custom(255, 128, 0).to_string(), "#FF8000");
    }

    #[test]
    fn test_color_custom_zeros() {
        assert_eq!(Color::Custom(0, 0, 0).to_string(), "#000000");
    }

    #[test]
    fn test_color_dynamic() {
        let cases = vec![
            (Color::Custom(128, 128, 128), "#808080"),
            (Color::Custom(255, 255, 255), "#FFFFFF"),
            (Color::Custom(1, 2, 3), "#010203"),
        ];
        for (color, expected) in cases {
            assert_eq!(color.to_string(), expected);
        }
    }
