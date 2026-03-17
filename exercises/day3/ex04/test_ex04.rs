    #[test]
    fn test_double_some() {
        assert_eq!(double_option(Some(5)), Some(10));
    }

    #[test]
    fn test_double_none() {
        assert_eq!(double_option(None), None);
    }

    #[test]
    fn test_add_options_both_some() {
        assert_eq!(add_options(Some(3), Some(4)), Some(7));
    }

    #[test]
    fn test_add_options_one_none() {
        assert_eq!(add_options(Some(3), None), None);
        assert_eq!(add_options(None, Some(4)), None);
    }

    #[test]
    fn test_add_options_both_none() {
        assert_eq!(add_options(None, None), None);
    }

    #[test]
    fn test_option_dynamic() {
        let values: Vec<(Option<i32>, Option<i32>)> = vec![
            (Some(0), Some(0)), (Some(-5), Some(5)),
            (Some(100), None), (None, None),
        ];
        for (a, b) in values {
            let expected = match (a, b) {
                (Some(x), Some(y)) => Some(x + y),
                _ => None,
            };
            assert_eq!(add_options(a, b), expected, "Failed for add_options({:?}, {:?})", a, b);
        }
    }
