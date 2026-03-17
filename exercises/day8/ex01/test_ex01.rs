    #[test]
    fn test_eval_rpn() {
        assert_eq!(eval_rpn(&["2","1","+","3","*"]), 9);
        assert_eq!(eval_rpn(&["4","13","5","/","+"]), 6);
        assert_eq!(eval_rpn(&["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22);
    }
