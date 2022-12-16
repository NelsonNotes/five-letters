export interface TState<D, E> {
	loading: boolean
	data: D | null
	error: E | null
}
