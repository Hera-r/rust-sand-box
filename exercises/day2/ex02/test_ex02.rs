    #[test]
    fn test_swap_basic() {
        let mut a = 1;
        let mut b = 2;
        swap_values(&mut a, &mut b);
        assert_eq!(a, 2);
        assert_eq!(b, 1);
    }

    #[test]
    fn test_swap_same() {
        let mut a = 42;
        let mut b = 42;
        swap_values(&mut a, &mut b);
        assert_eq!(a, 42);
        assert_eq!(b, 42);
    }

    #[test]
    fn test_swap_negative() {
        let mut a = -10;
        let mut b = 20;
        swap_values(&mut a, &mut b);
        assert_eq!(a, 20);
        assert_eq!(b, -10);
    }

    #[test]
    fn test_swap_dynamic() {
        let pairs: Vec<(i32, i32)> = vec![(0, 0), (100, -100), (i32::MIN, i32::MAX), (7, 13)];
        for (orig_a, orig_b) in pairs {
            let mut a = orig_a;
            let mut b = orig_b;
            swap_values(&mut a, &mut b);
            assert_eq!(a, orig_b, "After swap, a should be {}", orig_b);
            assert_eq!(b, orig_a, "After swap, b should be {}", orig_a);
        }
    }
