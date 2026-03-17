    #[test]
    fn test_parallel_sum() {
        assert_eq!(parallel_sum(vec![1, 2, 3, 4]), 10);
        assert_eq!(parallel_sum(vec![]), 0);
        let big: Vec<i32> = vec![1; 1000];
        assert_eq!(parallel_sum(big), 1000);
    }
