package main

import (
	"bufio"
	"fmt"
	"os"
)

type SegTree struct {
	n    int
	mn   []int64
	lazy []int64
}

func NewSegTree(size int) *SegTree {
	st := &SegTree{}
	st.init(size)
	return st
}

func (st *SegTree) init(size int) {
	st.n = 1
	for st.n < size {
		st.n <<= 1
	}
	st.mn = make([]int64, 2*st.n)
	st.lazy = make([]int64, 2*st.n)
	for i := range st.mn {
		st.mn[i] = 1e18
	}
}

func (st *SegTree) buildFrom(a []int64) {
	m := len(a)
	for i := 0; i < m; i++ {
		st.mn[st.n+i] = a[i]
	}
	for i := st.n - 1; i >= 1; i-- {
		st.mn[i] = min(st.mn[i<<1], st.mn[i<<1|1])
	}
}

func (st *SegTree) apply(idx int, val int64) {
	st.mn[idx] += val
	st.lazy[idx] += val
}

func (st *SegTree) push(idx int) {
	if st.lazy[idx] != 0 {
		st.apply(idx<<1, st.lazy[idx])
		st.apply(idx<<1|1, st.lazy[idx])
		st.lazy[idx] = 0
	}
}

func (st *SegTree) pull(idx int) {
	st.mn[idx] = min(st.mn[idx<<1], st.mn[idx<<1|1])
}

func (st *SegTree) rangeAdd(l, r int, val int64) {
	if l > r {
		return
	}
	st.rangeAddRec(1, 0, st.n-1, l, r, val)
}

func (st *SegTree) rangeAddRec(idx, nl, nr, l, r int, val int64) {
	if l > nr || r < nl {
		return
	}
	if l <= nl && nr <= r {
		st.apply(idx, val)
		return
	}
	st.push(idx)
	mid := (nl + nr) >> 1
	st.rangeAddRec(idx<<1, nl, mid, l, r, val)
	st.rangeAddRec(idx<<1|1, mid+1, nr, l, r, val)
	st.pull(idx)
}

func (st *SegTree) findFirstNegative(origN int) int {
	if st.mn[1] >= 0 {
		return -1
	}
	return st.findFirstNegativeRec(1, 0, st.n-1, origN)
}

func (st *SegTree) findFirstNegativeRec(idx, nl, nr, origN int) int {
	if nl > origN-1 {
		return -1
	}
	if nl == nr {
		if st.mn[idx] < 0 {
			return nl
		}
		return -1
	}
	st.push(idx)
	mid := (nl + nr) >> 1
	res := st.findFirstNegativeRec(idx<<1, nl, mid, origN)
	if res != -1 {
		return res
	}
	return st.findFirstNegativeRec(idx<<1|1, mid+1, nr, origN)
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var ac, dr int
	if _, err := fmt.Fscan(reader, &ac, &dr); err != nil {
		return
	}

	var n int
	fmt.Fscan(reader, &n)
	a := make([]int, n+1)
	d := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(reader, &a[i])
	}
	for i := 1; i <= n; i++ {
		fmt.Fscan(reader, &d[i])
	}

	calcNeed := func(ai, di int) int {
		val := max(ai-ac, 0) + max(di-dr, 0)
		if val > n {
			val = n
		}
		return val
	}

	need := make([]int, n+1)
	cnt := make([]int, n+1)
	for i := 1; i <= n; i++ {
		need[i] = calcNeed(a[i], d[i])
		cnt[need[i]]++
	}

	B := make([]int64, n)
	pref := 0
	for i := 0; i <= n-1; i++ {
		pref += cnt[i]
		B[i] = int64(pref - (i + 1))
	}

	seg := NewSegTree(n)
	seg.buildFrom(B)

	var m int
	fmt.Fscan(reader, &m)
	for i := 0; i < m; i++ {
		var k, na, nd int
		fmt.Fscan(reader, &k, &na, &nd)
		old := need[k]
		if old <= n-1 {
			seg.rangeAdd(old, n-1, -1)
			cnt[old]--
		} else {
			cnt[old]--
		}
		need[k] = calcNeed(na, nd)
		nw := need[k]
		if nw <= n-1 {
			seg.rangeAdd(nw, n-1, 1)
			cnt[nw]++
		} else {
			cnt[nw]++
		}
		a[k] = na
		d[k] = nd
		idx := seg.findFirstNegative(n)
		ans := n
		if idx != -1 {
			ans = idx
		}
		fmt.Fprintln(writer, ans)}}
func max(a, b int) int {
	if a > b {
		return a}
	return b}