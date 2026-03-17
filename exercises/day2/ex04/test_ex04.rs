    #[test]
    fn test_count_chars_simple() {
        assert_eq!(count_chars("hello"), 5);
    }

    #[test]
    fn test_count_chars_empty() {
        assert_eq!(count_chars(""), 0);
    }

    #[test]
    fn test_count_chars_unicode() {
        assert_eq!(count_chars("héllo"), 5);
    }

    #[test]
    fn test_count_chars_spaces() {
        assert_eq!(count_chars("hello world"), 11);
    }

    #[test]
    fn test_count_chars_dynamic() {
        let cases = vec![
            ("rust", 4), ("a", 1), ("ab cd ef", 8),
            ("🦀", 1), ("hello🦀world", 11),
        ];
        for (input, expected) in cases {
            assert_eq!(count_chars(input), expected, "Failed for count_chars(\"{}\")", input);
        }
    }
