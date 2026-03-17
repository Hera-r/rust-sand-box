    #[test]
    fn test_longest_first() {
        assert_eq!(longest("hello", "hi"), "hello");
    }

    #[test]
    fn test_longest_second() {
        assert_eq!(longest("hi", "hello"), "hello");
    }

    #[test]
    fn test_longest_equal() {
        let result = longest("abc", "xyz");
        assert!(result == "abc" || result == "xyz");
    }

    #[test]
    fn test_longest_empty() {
        assert_eq!(longest("", "hello"), "hello");
        assert_eq!(longest("world", ""), "world");
    }

    #[test]
    fn test_longest_dynamic() {
        let cases = vec![
            ("rust", "python", "python"),
            ("a", "ab", "ab"),
            ("ownership", "borrow", "ownership"),
        ];
        for (a, b, expected) in cases {
            assert_eq!(longest(a, b), expected, "Failed for longest(\"{}\", \"{}\")", a, b);
        }
    }
