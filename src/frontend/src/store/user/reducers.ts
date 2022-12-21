import { createSlice } from '@reduxjs/toolkit'

import { TUserState } from '../../types/user'
import { fetch } from './actions'

const initialState: TUserState = {
	loading: false,
	data: null,
	error: null,
}

export const userSlice = createSlice({
	name: 'user',
	initialState,
	reducers: {},
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

export default userSlice.reducer
