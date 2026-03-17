    #[test]
    fn test_calc_add() {
        assert!((calculate(Operation::Add(2.0, 3.0)) - 5.0).abs() < 0.01);
    }

    #[test]
    fn test_calc_subtract() {
        assert!((calculate(Operation::Subtract(10.0, 4.0)) - 6.0).abs() < 0.01);
    }

    #[test]
    fn test_calc_multiply() {
        assert!((calculate(Operation::Multiply(3.0, 7.0)) - 21.0).abs() < 0.01);
    }

    #[test]
    fn test_calc_divide() {
        assert!((calculate(Operation::Divide(10.0, 2.0)) - 5.0).abs() < 0.01);
    }

    #[test]
    fn test_calc_divide_by_zero() {
        assert!(calculate(Operation::Divide(10.0, 0.0)).is_nan()
            || calculate(Operation::Divide(10.0, 0.0)).is_infinite());
    }

    #[test]
    fn test_calc_dynamic() {
        let cases: Vec<(Operation, f64)> = vec![
            (Operation::Add(-5.0, 5.0), 0.0),
            (Operation::Subtract(0.0, 0.0), 0.0),
            (Operation::Multiply(100.0, 0.01), 1.0),
            (Operation::Divide(100.0, 4.0), 25.0),
        ];
        for (op, expected) in cases {
            assert!((calculate(op) - expected).abs() < 0.01);
        }
    }
