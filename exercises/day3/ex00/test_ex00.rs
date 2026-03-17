    #[test]
    fn test_rectangle_area() {
        let rect = Rectangle::new(10.0, 5.0);
        assert!((rect.area() - 50.0).abs() < 0.01);
    }

    #[test]
    fn test_rectangle_perimeter() {
        let rect = Rectangle::new(10.0, 5.0);
        assert!((rect.perimeter() - 30.0).abs() < 0.01);
    }

    #[test]
    fn test_rectangle_is_square() {
        let sq = Rectangle::new(5.0, 5.0);
        assert!(sq.is_square());
        let rect = Rectangle::new(5.0, 3.0);
        assert!(!rect.is_square());
    }

    #[test]
    fn test_rectangle_dynamic() {
        let cases: Vec<(f64, f64, f64, f64)> = vec![
            (1.0, 1.0, 1.0, 4.0),
            (3.0, 4.0, 12.0, 14.0),
            (100.0, 200.0, 20000.0, 600.0),
            (0.5, 0.5, 0.25, 2.0),
        ];
        for (w, h, exp_area, exp_perim) in cases {
            let r = Rectangle::new(w, h);
            assert!((r.area() - exp_area).abs() < 0.01, "area failed for {}x{}", w, h);
            assert!((r.perimeter() - exp_perim).abs() < 0.01, "perimeter failed for {}x{}", w, h);
        }
    }
