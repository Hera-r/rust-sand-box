    #[test]
    fn test_parallel_map() {
        assert_eq!(parallel_map(vec![1,2,3,4], |x| x * x), vec![1, 4, 9, 16]);
        assert_eq!(parallel_map(vec![10,20], |x| x + 5), vec![15, 25]);
        assert_eq!(parallel_map(vec![], |x| x), Vec::<i32>::new());
    }
