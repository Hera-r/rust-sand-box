    #[test]
    fn test_valid_parentheses() {
        assert_eq!(valid_parentheses("()[]{}"), true);
        assert_eq!(valid_parentheses("([)]"), false);
        assert_eq!(valid_parentheses("{[]}"), true);
        assert_eq!(valid_parentheses(""), true);
        assert_eq!(valid_parentheses("("), false);
    }
