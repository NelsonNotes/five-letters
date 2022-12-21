import { createSlice } from '@reduxjs/toolkit'

import { TSessionState } from '../../types/session'
import { fetch } from './actions'
import { sessionPull } from './utils'

const initialState: TSessionState = {
	loading: false,
	data: sessionPull(),
	error: null,
}

export const sessionSlice = createSlice({
	name: 'session',
	initialState,
	reducers: {
		clear: (state) => {
			state.loading = false
			state.data = null
			state.error = null
		},
	},
	extraReducers: (builder) => {
		builder
			.addCase(fetch.pending, (state) => {
				state.loading = true
			})
			.addCase(fetch.fulfilled, (state, action) => {
				state.loading = false
				state.data = action.payload
				state.error = null
			})
			.addCase(fetch.rejected, (state, action) => {
				state.loading = false
				state.data = state.data
				state.error = action.error
			})
	},
})

export const { clear } = sessionSlice.actions

export default sessionSlice.reducer
