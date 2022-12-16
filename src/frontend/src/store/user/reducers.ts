import { createSlice } from '@reduxjs/toolkit'

import { TUserState } from '../../types/user'
import { fetchUser } from './actions'

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
			.addCase(fetchUser.pending, (state) => {
				state.loading = true
			})
			.addCase(fetchUser.fulfilled, (state, action) => {
				state.loading = false
				state.data = action.payload
				state.error = null
			})
			.addCase(fetchUser.rejected, (state, action) => {
				state.loading = false
				state.data = null
				state.error = action.error
			})
	},
})

export default userSlice.reducer
