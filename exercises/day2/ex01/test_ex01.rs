    #[test]
    fn test_concat_basic() {
        assert_eq!(concat_strings("hello", " world"), "hello world");
    }

    #[test]
    fn test_concat_empty() {
        assert_eq!(concat_strings("", "rust"), "rust");
        assert_eq!(concat_strings("rust", ""), "rust");
    }

    #[test]
    fn test_concat_both_empty() {
        assert_eq!(concat_strings("", ""), "");
    }

    #[test]
    fn test_concat_dynamic() {
        let pairs = vec![
            ("foo", "bar", "foobar"),
            ("hello", "!", "hello!"),
            ("rust", "acean", "rustacean"),
            ("1234", "5678", "12345678"),
        ];
        for (a, b, expected) in pairs {
            assert_eq!(concat_strings(a, b), expected, "Failed for concat_strings(\"{}\", \"{}\")", a, b);
        }
    }
