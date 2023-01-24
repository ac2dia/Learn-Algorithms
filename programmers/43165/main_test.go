package main

import "testing"

func Test_solution(t *testing.T) {
	type args struct {
		numbers []int
		target  int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{
			name: "t1",
			args: args{numbers: []int{1, 1, 1, 1, 1}, target: 3},
			want: 5,
		},
		{
			name: "t2",
			args: args{numbers: []int{4, 1, 2, 1}, target: 4},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solution(tt.args.numbers, tt.args.target); got != tt.want {
				t.Errorf("solution() = %v, want %v", got, tt.want)
			}
		})
	}
}
