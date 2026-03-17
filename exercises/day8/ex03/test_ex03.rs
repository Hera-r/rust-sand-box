    #[test]
    fn test_game_of_life() {
        let grid = vec![
            vec![false, true, false],
            vec![false, true, false],
            vec![false, true, false],
        ];
        let next = next_generation(grid);
        assert_eq!(next, vec![
            vec![false, false, false],
            vec![true, true, true],
            vec![false, false, false],
        ]);
    }
