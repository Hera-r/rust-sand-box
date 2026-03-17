    #[test]
    fn test_transpose_2x2() {
        let matrix = vec![vec![1, 2], vec![3, 4]];
        assert_eq!(transpose(matrix), vec![vec![1, 3], vec![2, 4]]);
    }

    #[test]
    fn test_transpose_3x3() {
        let matrix = vec![
            vec![1, 2, 3],
            vec![4, 5, 6],
            vec![7, 8, 9],
        ];
        let expected = vec![
            vec![1, 4, 7],
            vec![2, 5, 8],
            vec![3, 6, 9],
        ];
        assert_eq!(transpose(matrix), expected);
    }

    #[test]
    fn test_transpose_1x1() {
        assert_eq!(transpose(vec![vec![42]]), vec![vec![42]]);
    }

    #[test]
    fn test_transpose_2x3() {
        let matrix = vec![vec![1, 2, 3], vec![4, 5, 6]];
        let expected = vec![vec![1, 4], vec![2, 5], vec![3, 6]];
        assert_eq!(transpose(matrix), expected);
    }

    #[test]
    fn test_transpose_identity() {
        let matrix = vec![
            vec![1, 0, 0],
            vec![0, 1, 0],
            vec![0, 0, 1],
        ];
        assert_eq!(transpose(matrix.clone()), matrix);
    }
