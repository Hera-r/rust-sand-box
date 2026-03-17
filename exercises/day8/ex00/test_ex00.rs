    #[test]
    fn test_matrix_multiply() {
        let a = vec![vec![1,2], vec![3,4]];
        let b = vec![vec![5,6], vec![7,8]];
        assert_eq!(matrix_multiply(&a, &b), vec![vec![19,22], vec![43,50]]);
        
        let id = vec![vec![1,0], vec![0,1]];
        assert_eq!(matrix_multiply(&a, &id), a);
    }
