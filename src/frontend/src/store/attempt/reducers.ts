import { createSlice } from '@reduxjs/toolkit'
import { TAttemptState } from '../../types/attempt'

import { make } from './actions'

const initialState: TAttemptState = {
	loading: false,
	data: null,
	error: null,
}

export const attemptSlice = createSlice({
	name: 'attempt',
	initialState,
	reducers: {},
	extraReducers: (builder) => {
		builder
			.addCase(make.pending, (state) => {
				state.loading = true
			})
			.addCase(make.fulfilled, (state, action) => {
				state.loading = false
				state.data = action.payload
				state.error = null
			})
			.addCase(make.rejected, (state, action) => {
				state.loading = false
				state.data = null
				state.error = action.error
			})
	},
})

export default attemptSlice.reducer
