    #[test]
    fn test_first_word_simple() {
        assert_eq!(first_word("hello world"), "hello");
    }

    #[test]
    fn test_first_word_single() {
        assert_eq!(first_word("rust"), "rust");
    }

    #[test]
    fn test_first_word_leading_spaces() {
        assert_eq!(first_word("  hello world"), "hello");
    }

    #[test]
    fn test_first_word_empty() {
        assert_eq!(first_word(""), "");
    }

    #[test]
    fn test_first_word_dynamic() {
        let cases = vec![
            ("the quick brown fox", "the"),
            ("ownership matters", "ownership"),
            ("a", "a"),
            ("   spaces   everywhere", "spaces"),
        ];
        for (input, expected) in cases {
            assert_eq!(first_word(input), expected, "Failed for first_word(\"{}\")", input);
        }
    }
