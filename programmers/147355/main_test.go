package main

import "testing"

func Test_solution(t *testing.T) {
	type args struct {
		t string
		p string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{
			name: "t1",
			args: args{t: "3141592", p: "271"},
			want: 2,
		},
		{
			name: "t2",
			args: args{t: "500220839878", p: "7"},
			want: 8,
		},
		{
			name: "t3",
			args: args{t: "10203", p: "15"},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := solution(tt.args.t, tt.args.p); got != tt.want {
				t.Errorf("solution() = %v, want %v", got, tt.want)
			}
		})
	}
}
