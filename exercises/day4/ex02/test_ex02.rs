    #[test]
    fn test_flatten_basic() {
        assert_eq!(flatten(vec![vec![1, 2], vec![3, 4]]), vec![1, 2, 3, 4]);
    }

    #[test]
    fn test_flatten_empty() {
        let empty: Vec<Vec<i32>> = vec![];
        assert_eq!(flatten(empty), Vec::<i32>::new());
    }

    #[test]
    fn test_flatten_single() {
        assert_eq!(flatten(vec![vec![1, 2, 3]]), vec![1, 2, 3]);
    }

    #[test]
    fn test_flatten_empty_inner() {
        assert_eq!(flatten(vec![vec![], vec![1], vec![]]), vec![1]);
    }

    #[test]
    fn test_flatten_dynamic() {
        let input: Vec<Vec<i32>> = (0..10).map(|i| vec![i * 2, i * 2 + 1]).collect();
        let result = flatten(input);
        let expected: Vec<i32> = (0..20).collect();
        assert_eq!(result, expected);
    }
