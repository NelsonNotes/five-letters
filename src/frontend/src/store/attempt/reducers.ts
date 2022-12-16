import { createSlice } from '@reduxjs/toolkit'
import { TAttemptState } from '../../types/attempt'

import { makeAttempt } from './actions'

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
			.addCase(makeAttempt.pending, (state) => {
				state.loading = true
			})
			.addCase(makeAttempt.fulfilled, (state, action) => {
				state.loading = false
				state.data = action.payload
				state.error = null
			})
			.addCase(makeAttempt.rejected, (state, action) => {
				state.loading = false
				state.data = null
				state.error = action.error
			})
	},
})

export default attemptSlice.reducer
