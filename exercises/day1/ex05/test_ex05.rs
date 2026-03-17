    #[test]
    fn test_celsius_to_fahrenheit_boiling() {
        assert!((celsius_to_fahrenheit(100.0) - 212.0).abs() < 0.01);
    }

    #[test]
    fn test_celsius_to_fahrenheit_freezing() {
        assert!((celsius_to_fahrenheit(0.0) - 32.0).abs() < 0.01);
    }

    #[test]
    fn test_celsius_to_fahrenheit_body() {
        assert!((celsius_to_fahrenheit(37.0) - 98.6).abs() < 0.01);
    }

    #[test]
    fn test_celsius_to_fahrenheit_negative() {
        assert!((celsius_to_fahrenheit(-40.0) - (-40.0)).abs() < 0.01);
    }

    #[test]
    fn test_celsius_to_fahrenheit_dynamic() {
        let values: Vec<f64> = vec![0.0, 10.0, 20.0, 25.5, -10.0, -273.15, 50.0, 75.5];
        for c in values {
            let expected = c * 9.0 / 5.0 + 32.0;
            assert!(
                (celsius_to_fahrenheit(c) - expected).abs() < 0.01,
                "Failed for celsius_to_fahrenheit({}): expected {}, got {}",
                c, expected, celsius_to_fahrenheit(c)
            );
        }
    }
