import { createSlice } from '@reduxjs/toolkit'

import { TSessionState } from '../../types/session'
import { fetchSession } from './actions'

const initialState: TSessionState = {
	loading: false,
	data: null,
	error: null,
}

export const sessionSlice = createSlice({
	name: 'session',
	initialState,
	reducers: {},
	extraReducers: (builder) => {
		builder
			.addCase(fetchSession.pending, (state) => {
				state.loading = true
			})
			.addCase(fetchSession.fulfilled, (state, action) => {
				state.loading = false
				state.data = action.payload
				state.error = null
			})
			.addCase(fetchSession.rejected, (state, action) => {
				state.loading = false
				state.data = null
				state.error = action.error
			})
	},
})

export default sessionSlice.reducer
